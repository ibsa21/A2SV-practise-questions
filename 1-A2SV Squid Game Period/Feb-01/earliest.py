class Solution:
    def earliestFullBloom(self, floweringTime: List[int], growthTime: List[int]) -> int:
        sortedPlants = sorted(zip(growthTime,floweringTime), reverse = True)
   
        totalGrowthTime = 0
        availableTimeToPlant = 0
        
        for growPeriod, flowerPeriod in sortedPlants:
            if availableTimeToPlant >= flowerPeriod:
                availableTimeToPlant -= flowerPeriod
                
                if availableTimeToPlant < growPeriod:
                    totalGrowthTime += growPeriod - availableTimeToPlant 
                    availableTimeToPlant = growPeriod
                    
            else:
                totalGrowthTime += flowerPeriod
                totalGrowthTime += growPeriod - availableTimeToPlant 
                availableTimeToPlant = growPeriod
        
        return totalGrowthTime
