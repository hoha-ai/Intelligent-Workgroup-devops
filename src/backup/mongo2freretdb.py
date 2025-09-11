import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# 源数据库连接信息
source_uri = "mongodb://10.42.0.88:27017/"

# 目标数据库连接信息
target_uri = "mongodb://10.42.0.82:27017/"

def migrate_mongo():
    """
    将一个 MongoDB 实例的所有数据库和集合迁移到另一个实例。
    """
    try:
        # 1. 连接源和目标数据库
        print("正在连接到源数据库...")
        source_client = MongoClient(source_uri)
        # 触发连接以检查有效性
        source_client.admin.command('ping') 
        print("源数据库连接成功。")

        print("正在连接到目标数据库...")
        target_client = MongoClient(target_uri)
        # 触发连接以检查有效性
        target_client.admin.command('ping')
        print("目标数据库连接成功。")

    except ConnectionFailure as e:
        print(f"数据库连接失败: {e}")
        return

    try:
        # 2. 获取源数据库列表
        # 排除系统数据库
        system_dbs = {'admin', 'config', 'local'}
        source_db_names = [db_name for db_name in source_client.list_database_names() if db_name not in system_dbs]
        
        if not source_db_names:
            print("源服务器上没有找到需要迁移的用户数据库。")
            return

        print(f"发现需要迁移的数据库: {', '.join(source_db_names)}")

        total_dbs = len(source_db_names)
        
        # 3. 遍历数据库
        for i, db_name in enumerate(source_db_names, 1):
            print(f"\n--- 开始迁移数据库: {db_name} ({i}/{total_dbs}) ---")
            
            source_db = source_client[db_name]
            target_db = target_client[db_name]
            
            collection_names = source_db.list_collection_names()
            
            if not collection_names:
                print(f"数据库 '{db_name}' 中没有集合，跳过。")
                continue

            total_colls = len(collection_names)

            # 4. 遍历集合并迁移数据
            for j, collection_name in enumerate(collection_names, 1):
                print(f"  - 正在迁移集合: {collection_name} ({j}/{total_colls})")
                
                source_collection = source_db[collection_name]
                target_collection = target_db[collection_name]
                
                # 为了防止目标集合已存在并含有旧数据，可以选择先清空
                # 注意：这是一个危险操作，请根据你的需求决定是否启用！
                # print(f"    - 清空目标集合 '{collection_name}'...")
                # target_collection.delete_many({})

                documents_count = 0
                try:
                    # 使用 find().batch_size() 可以有效控制内存使用
                    cursor = source_collection.find({}, no_cursor_timeout=True).batch_size(1000)
                    documents_to_insert = []
                    
                    for doc in cursor:
                        documents_to_insert.append(doc)
                        documents_count += 1
                        
                        # 每 1000 条文档批量插入一次
                        if len(documents_to_insert) >= 1000:
                            target_collection.insert_many(documents_to_insert)
                            documents_to_insert = []
                            print(f"\r    - 已迁移 {documents_count} 个文档...", end="")
                    
                    # 插入剩余的文档
                    if documents_to_insert:
                        target_collection.insert_many(documents_to_insert)
                    
                    print(f"\r    - 集合 '{collection_name}' 迁移完成，共 {documents_count} 个文档。")

                except Exception as e:
                    print(f"\n迁移集合 '{collection_name}' 时发生错误: {e}")
                finally:
                    if 'cursor' in locals() and cursor:
                        cursor.close()

            print(f"--- 数据库 '{db_name}' 迁移完成 ---")

        print("\n所有数据库迁移任务已完成！")

    except Exception as e:
        print(f"迁移过程中发生未知错误: {e}")
    finally:
        # 关闭连接
        if 'source_client' in locals() and source_client:
            source_client.close()
            print("\n源数据库连接已关闭。")
        if 'target_client' in locals() and target_client:
            target_client.close()
            print("目标数据库连接已关闭。")


if __name__ == "__main__":
    migrate_mongo()

