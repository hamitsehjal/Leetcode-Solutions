class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function subsetsWithDup($nums) {
        sort($nums);
        $this->ans = [];
        $this->nums = $nums;
        $this->backtrack([],0);
        return $this->ans;
    }

    function backtrack($cur,$index){
        $this->ans[] = $cur;

        for($i=$index;$i<count($this->nums);$i++){
            if($i > $index && $this->nums[$i] == $this->nums[$i-1]){
                continue;
            }
            $cur[] = $this->nums[$i];
            $this->backtrack($cur,$i+1);
            array_pop($cur);
        }
    }
}