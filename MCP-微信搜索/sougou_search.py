from miku_ai import get_wexin_article
import asyncio
import json
import sys # 导入 sys 模块

async def main():
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("Usage: python scr.py <query_value>")
        sys.exit(1) # 如果没有提供查询值，则退出

    query = sys.argv[1] # 获取第一个命令行参数作为查询值
    
    articles = await get_wexin_article(query)
    
    output_articles = []
    for article in articles:
        output_articles.append({
            "title": article['title'],
            "url": article['url'],
            "source": article['source'],
            "date": article['date']
        })
    
    print(json.dumps(output_articles, ensure_ascii=False, indent=4))

asyncio.run(main())
