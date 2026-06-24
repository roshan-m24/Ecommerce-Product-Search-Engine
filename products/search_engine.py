
def search_rank(products,query):
    q=query.lower()
    ranked=[]
    for p in products:
        tags=[x.strip().lower() for x in p.tags.split(',')]
        if q in p.category.lower() or q.rstrip('s') in p.category.lower():
            score=0.9+min(len(tags)*0.01,0.09); reason='Category match'
        elif any(q==t for t in tags):
            score=0.8; reason='Tag match'
        elif any(q in t for t in tags):
            score=0.7; reason='Partial tag match'
        elif q in p.product_name.lower() or q in p.product_description.lower():
            score=0.5; reason='Description match'
        else:
            continue
        ranked.append((score,reason,p))
    return sorted(ranked,key=lambda x:x[0],reverse=True)
