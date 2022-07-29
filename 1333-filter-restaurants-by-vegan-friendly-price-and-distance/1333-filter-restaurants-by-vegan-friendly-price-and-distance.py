from sortedcontainers import SortedList
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        result = SortedList()
        
        for r_id, r_rating, is_vegan, r_price, r_distance in restaurants:
            if r_price <= maxPrice and r_distance <= maxDistance:
                if veganFriendly == True:
                    if is_vegan==True:result.add((r_rating, r_id))
                else:result.add((r_rating, r_id))
        return [result[i][1] for i in range(len(result)-1, -1, -1)]