class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        preq_recipe = defaultdict(list)
        req_counter = [0] * len(recipes)
        set_recipes = set(recipes)
        set_supplies = set(supplies)
        
        for idx, ingredient in enumerate(ingredients):
            for ingr in ingredient:
                if ingr in set_recipes:
                    preq_recipe[ingr].append(idx)
                    req_counter[idx] += 1
                if ingr not in set_recipes and  ingr not in set_supplies:
                    req_counter[idx] = float(inf)
        print(preq_recipe, req_counter)
        
        q = deque()
        ans  = []
        for idx, req_recipe in enumerate(req_counter):
            if req_recipe==0:
                q.append(idx)
                ans.append(recipes[idx])
        
        print(q)
        while q:
            cur_recipe_idx = q.pop()
            
            for newRecipe in preq_recipe[recipes[cur_recipe_idx]]:
                req_counter[newRecipe]-=1
                if req_counter[newRecipe]==0:
                    q.append(newRecipe)
                    ans.append(recipes[newRecipe])
        print(ans)
        return ans