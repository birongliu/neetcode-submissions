class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length) return false;

        let Scount = {}, Tcount = {};
        //loop over the count of each letter
        for(let i = 0; i < s.length; i++) {
            Scount[s[i]] = (Scount[s[i]] + 1 || 0);
            Tcount[t[i]] = (Tcount[t[i]] + 1 || 0);
        }
        for(let key in Scount) {
            if(Scount[key] !== Tcount[key]) return false;
        }
        return true;
    }
}
