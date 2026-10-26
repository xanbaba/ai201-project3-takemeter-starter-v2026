// Run after prepare_dataset.py in an environment with @oai/artifact-tool.
// The complete source strings are written as literal cell values, then exported
// to the assignment's CSV format without an Excel-length or display truncation.
import fs from 'node:fs/promises';
import path from 'node:path';
import { Workbook } from '@oai/artifact-tool';

const root = process.cwd();
const sources = JSON.parse(await fs.readFile(path.join(root, 'data/source_posts.json'), 'utf8'));
const rows = [['text', 'label', 'note'], ...sources.map(p => [
  p.title + (p.body ? '\n\n' + p.body : ''), p.label, p.note,
])];
const workbook = Workbook.create();
const sheet = workbook.worksheets.add('Labels');
const range = sheet.getRange(`A1:C${rows.length}`);
range.values = rows;
workbook.recalculate();
const actual = range.values;
if (JSON.stringify(actual) !== JSON.stringify(rows)) {
  throw new Error('Cell values changed while authoring; refusing to export.');
}
// CSV quoting preserves all embedded newlines, commas, quotes, and Unicode.
const quote = value => '"' + String(value).replaceAll('"', '""') + '"';
const csv = actual.map(row => row.map(quote).join(',')).join('\r\n') + '\r\n';
await fs.writeFile(path.join(root, 'labels.csv'), csv, 'utf8');
console.log(`Wrote labels.csv with ${actual.length - 1} complete posts.`);
