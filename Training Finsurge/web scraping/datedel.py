from elasticsearch import Elasticsearch 
es = Elasticsearch("http://localhost:9200") 

delete_query = {
    "query" : {
        "range":{
            "date":{
                "lt": "now-1d/d"
            }
        }
    }
} 
before = es.count(index="news_index")["count"] 
print("Total rows before deleted : ",before) 

response = es.delete_by_query(index="news_index",body=delete_query,refresh=True)
print("Deleted Successfully",response["deleted"]) 

after = es.count(index="news_index")["count"] 
print("Total rows After deleted : ",after) 

