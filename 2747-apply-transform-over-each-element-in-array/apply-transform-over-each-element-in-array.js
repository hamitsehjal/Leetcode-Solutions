/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
    new_arr = [];
    for (let i = 0; i < arr.length; i++) {
        const item = arr[i];
        new_arr.push(fn(item, i))
    }

    return new_arr
};