class Solution:

    def encode(self, strs: List[str]) -> str:
        if (not strs):
            return ""
        enc = ""
        for s in strs: 
            enc += str(len(s)) + '#' + s;
        return enc

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        num_char_str = ""
        dec = ""
        dec_arr = []
        # enable for getting string length
        scan_len = 1
        for c in s:
            # move on to next character if # seen
            if (scan_len and c == '#'):
                # disable scanning string length
                scan_len = 0
                # cast string length into int
                num_char = int(num_char_str)
                num_char_str = ""
                # edge case of empty string
                if (num_char == 0):
                    dec_arr.append("")
                    scan_len = 1
                continue
            elif (scan_len):
                num_char_str += c
            # after # seen, start building string
            # build string
            elif (not scan_len and num_char > 0):
                dec += c
                # decrement count after add
                num_char -= 1
                if (num_char == 0):
                    dec_arr.append(dec)
                    scan_len = 1
                    dec = ""
        return dec_arr
