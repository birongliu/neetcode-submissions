class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let cache = {}

        for(let str of strs) {
            let key = str.split("").sort().join("");
            cache[key] ? cache[key].push(str) : cache[key] = [str] 
        }
        return Object.values(cache)
    }
}
