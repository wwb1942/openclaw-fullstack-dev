import cors from 'cors';
import express from 'express';

const app = express();
const port = Number(process.env.PORT || 3001);
const items = [{ id: 1, title: 'Wire the first end-to-end slice' }];

app.use(cors());
app.use(express.json());

app.get('/health', (_req, res) => {
  res.json({ ok: true });
});

app.get('/api/items', (_req, res) => {
  res.json(items);
});

app.post('/api/items', (req, res) => {
  const item = { id: items.length + 1, title: String(req.body.title || '') };
  items.push(item);
  res.status(201).json(item);
});

app.listen(port, () => {
  console.log(`server listening on ${port}`);
});
