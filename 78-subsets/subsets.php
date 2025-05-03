class Solution {

	/**
	* @param Integer[] $nums
	* @return Integer[][]
	*/
	function subsets($nums) {

		$ans = [];
        $backtrack=function($cur,$index)use($nums,&$ans,&$backtrack){
            $ans[]=$cur;
            for ($i = $index; $i < count($nums); $i++) {
                $cur[]=$nums[$i];
                $backtrack($cur,$i+1);
                array_pop($cur);
            }
        };
        
		$backtrack([],0);
        return $ans;
	}
}