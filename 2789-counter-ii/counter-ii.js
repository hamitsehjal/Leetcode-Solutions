/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {
    start = init
    return {
        increment: function () {
            return ++start
        },
        decrement: function () {
            return --start
        },
        reset: function () {
            start = init
            return start
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */