class Solution {

	/**
	* @param Integer[] $candidates
	* @param Integer $target
	* @return Integer[][]
	*/
	function combinationSum2($candidates, $target) {
        sort($candidates);
		$ans = [];
		$this->backtrack([], 0, 0, $target, $candidates, $ans);
		return $ans;
	}

    /** 
    * @param Integer[] $comb
    * @param Integer $curSum
    * @param Integer $index
    * @param Integer $target
    * @param Integer[] $candidates
    * @param Integer[] $ans
    */
	function backtrack($comb, $curSum, $index, $target, $candidates, &$ans) {
		if ($curSum === $target) {
			$ans[] = $comb;
			return;
		};

		if ($curSum > $target || $index >= count($candidates)) {
			return;
		};

		for ($i = $index; $i < count($candidates); $i++) {
            if ($i > $index && $candidates[$i] == $candidates[$i-1]){
                continue;
            }
			if ($curSum + $candidates[$i] <= $target) {
				$comb[] = $candidates[$i];
				$this->backtrack($comb, $curSum+$candidates[$i], $i+1, $target, $candidates, $ans);
				array_pop($comb);
			};
		};

	}
}