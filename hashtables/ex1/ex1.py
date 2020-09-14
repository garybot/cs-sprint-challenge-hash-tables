def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    
    for i in range(length):
        cache[weights[i]] = i

    for i in range(length):       
        if cache.get(limit - weights[i]):
            return [cache.get(limit - weights[i]), i]
            
    return None
