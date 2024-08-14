class Converter:
    def __init__(self, config: str, input: str) -> None:
        self.config = config
        self.input = input

    def convert(self) -> str:
        args = self.config.split("\n")
        lines = self.input.split("\n")

        matches = dict()
        counter = dict()

        for arg in args:
            elements = arg.split("=")
            matches[elements[0]] = elements[1]

        for idx in range(len(lines)):
            count = 0

            for m in matches.keys():
                count += lines[idx].count(m) * len(m)

                lines[idx] = lines[idx].replace(m, matches[m])

            counter[idx] = count

        sorted_lines = [lines[i] for i in sorted(counter, key=counter.get, reverse=True)]

        return "\n".join(sorted_lines)