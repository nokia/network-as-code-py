import fs from "fs";
import path from "path";

const __filename = new URL(import.meta.url).pathname;
const __dirname = path.dirname(__filename);

const deleteFolderRecursive = (folderPath) => {
  if (fs.existsSync(folderPath)) {
    fs.readdirSync(folderPath).forEach((file) => {
      const curPath = path.join(folderPath, file);
      if (fs.lstatSync(curPath).isDirectory()) {
        deleteFolderRecursive(curPath);
      } else {
        fs.unlinkSync(curPath);
      }
    });
    fs.rmdirSync(folderPath);
  }
};

const folder = process.argv.slice(2)[0];

if (folder) {
  deleteFolderRecursive(path.join(__dirname, "../dist", folder));
} else {
  deleteFolderRecursive(path.join(__dirname, "../dist/cjs"));
  deleteFolderRecursive(path.join(__dirname, "../dist/esm"));
  deleteFolderRecursive(path.join(__dirname, "../dist/@types"));
}
