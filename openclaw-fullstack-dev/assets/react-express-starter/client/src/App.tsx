import { useEffect, useState } from 'react';

const apiBase = import.meta.env.VITE_API_BASE_URL || 'http://localhost:3001';

export default function App() {
  const [items, setItems] = useState<{ id: number; title: string }[]>([]);

  useEffect(() => {
    fetch(`${apiBase}/api/items`)
      .then((res) => res.json())
      .then(setItems)
      .catch(() => setItems([]));
  }, []);

  return (
    <main style={{ maxWidth: 720, margin: '40px auto', fontFamily: 'sans-serif' }}>
      <h1>React + Express Starter</h1>
      <ul>{items.map((item) => <li key={item.id}>{item.title}</li>)}</ul>
    </main>
  );
}
