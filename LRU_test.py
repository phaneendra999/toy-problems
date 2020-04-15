
from LRU_cache import LRUCache

def main():
    checks = LRUCache(4)

    checks.put(1,10)
    
    checks.put(2,11)
    checks.put(3,12)
    assert checks.get_cache() == {1:10,2:11,3:12}
    assert checks.get(1) == 10
    assert checks.get(11) == -1
    checks.put(3,14)
    checks.put(4,13) 
    assert checks.get_cache() ==  {1:10,2:11,3:14,4:13}
    print("All test cases passed")
    
if __name__ == '__main__': 
    main()   