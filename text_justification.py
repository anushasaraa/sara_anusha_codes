class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        line = []
        currLen = 0

        for i, word in enumerate(words):

            # numSpaces represents the number of gaps between words currently in the line
            # If line has 1 word, gaps = 0. If 2 words, gaps = 1.
            numSpaces = len(line) - 1

            # Check if adding the new word overflows maxWidth
            # Logic: Existing Chars + Existing Min Gaps + New Gap (1) + New Word Length
            # Note: If numSpaces is -1 (empty line), this adds 0 for existing gaps.
            if currLen + numSpaces + 1 + len(word) > maxWidth:
                # Line is full. Justify the current line.
                remainder = maxWidth - currLen
                strLine = ""
                
                if numSpaces == 0:
                    # Single word case: Left justify (pad right)
                    strLine += line[0] + " " * remainder
                else:
                    # Multiple words case: Distribute spaces

                    # After each word we'll add "remainder // numSpaces" space and an extra single space if needed (not evenly divisible)
                    extraSpaces = remainder % numSpaces
                    for i in range(len(line) - 1):
                        # Add word + base spaces
                        strLine += line[i] + " " * (remainder // numSpaces)

                        # Add extra space if available (from left to right)
                        if extraSpaces > 0:
                            strLine += " "
                            extraSpaces -= 1

                    # Append the last word (no trailing spaces after it)
                    strLine += line[-1]

                output.append(strLine)
                # Reset line and currLen for the new line
                line = []
                currLen = 0
            
            # Add the current word to the (potentially new) line
            currLen += len(word)
            line.append(word)

        # Handle the last line (Left justified)
        if line:
            strLine = " ".join(line)
            # Pad the remainder with spaces to reach maxWidth
            strLine += " " * (maxWidth - len(strLine))
            output.append(strLine)

        return output
