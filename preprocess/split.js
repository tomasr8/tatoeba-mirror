const fs = require("fs");
const { findSourceMap } = require("module");

function shuffle(array) {
  let currentIndex = array.length;
  let randomIndex = 0;

  while (currentIndex != 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;
    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex],
      array[currentIndex],
    ];
  }
}

const pairs = [
  "en-it",
  "it-en",
  "en-fr",
  "fr-en",
  "en-cs",
  "cs-en",
  "it-fr",
  "fr-it",
  "it-cs",
  "cs-it",
  "fr-cs",
  "cs-fr",
];

const meta = {};

pairs.forEach((pair) => {
  const data = fs.readFileSync(`${pair}.tsv`, "utf-8");
  const lines = data.split("\n");
  shuffle(lines);

  const size = 2000;
  const files = Math.max(Math.floor(lines.length / size), 1);

  for (let i = 0; i < files; i++) {
    console.log(pair, i * size, (i + 1) * size);
    const slice = lines.slice(i * size, (i + 1) * size).map((line) => {
      const [, original, , translated] = line.trim().split("\t");
      return { original, translated };
    });

    fs.writeFileSync(
      `../public/data/${pair}-${i}.json`,
      JSON.stringify(slice),
      "utf-8"
    );
  }

  meta[pair] = files;
});

console.log(meta)
fs.writeFileSync("../public/data/meta.json", JSON.stringify(meta), "utf-8");
