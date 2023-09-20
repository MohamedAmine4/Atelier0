def bissextile( année : int ) -> bool :
    """_summary_

    Args:
        ann (int): Année

    Returns:
        bool: True = bissextile , False = non bissextile
    """
    return (année %4==0 and année %100!=0) or (année %4==0 and année %400==0 )

def test() :
    for i in range(2012,2025) :
        re=bissextile(i)
        print(i,"est",re)
        
# test()
