class Solution:
    def countCollisions(self, d: str) -> int:
        d=d.lstrip("L")
        d=d.rstrip("R")
        return d.count("L")+d.count("R")