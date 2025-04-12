class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        count = 0

        for rock in asteroids:
            if mass >= rock:
                count += 1
                mass += rock
            else:
                break

        return count == len(asteroids)
