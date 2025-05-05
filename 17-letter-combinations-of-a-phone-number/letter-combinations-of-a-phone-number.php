class Solution {

    /**
     * @param String $digits
     * @return String[]
     */
    function letterCombinations($digits) {
        $letterMapping = [
            '2' => ['a','b','c'],
            '3' => ['d','e','f'],
            '4' => ['g','h','i'],
            '5' => ['j','k','l'],
            '6' => ['m','n','o'],
            '7' => ['p','q','r','s'],
            '8' => ['t','u','v'],
            '9' => ['w','x','y','z'],
        ];
        if(empty($digits)){
            return [];
        }

        $ans = [];
        $backtrack = function($comb,$index)use(&$ans,&$backtrack,$letterMapping,$digits){
            if($index === strlen($digits)){
                $ans[] = implode("",$comb);
                return;
            }

            $digit = $digits[$index];
            foreach($letterMapping[$digit] as $letter){
                $comb[] = $letter;
                $backtrack($comb,$index+1);
                array_pop($comb);
            }
        };

        $backtrack([],0);
        return $ans;
    }
}