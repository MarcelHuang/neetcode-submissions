class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create pairs of (position, speed) for each car
        # Using zip to combine the two lists efficiently
        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        
        # Sort cars by position in descending order
        # This is crucial because:
        # 1. Cars can't pass each other
        # 2. We want to process cars from right to left (closer to target)
        cars.sort(reverse=True)
        
        # Initialize with first fleet
        # There will always be at least one fleet if there are cars
        fleets = 1
        
        # Calculate time to target for the first car (rightmost car)
        # time = distance / speed
        prev_time_to_target = (target - cars[0][0]) / cars[0][1]
        
        # Process remaining cars from right to left
        for i in range(1, len(cars)):
            curr_car = cars[i]
            
            # Calculate time to target for current car
            curr_time_to_target = (target - curr_car[0]) / curr_car[1]
            
            # If current car takes longer to reach target than previous car
            # it cannot catch up to form a fleet, so it becomes a new fleet
            if curr_time_to_target > prev_time_to_target:
                fleets += 1
                prev_time_to_target = curr_time_to_target
            
            # If current car would reach target sooner (curr_time <= prev_time)
            # it will catch up to previous car and join its fleet
            # No need to update prev_time as the slower car determines fleet speed
        
        return fleets