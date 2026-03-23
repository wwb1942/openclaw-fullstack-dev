'use client';

import { FormEvent, useEffect, useState } from 'react';

type Item = { id: number; title: string };

const apiBase = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:3001';

export default function Page() {
  const [items, setItems] = useState<Item[]>([]);
  const [title, setTitle] = useState('');
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function loadItems() {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(`${apiBase}/api/items`, { cache: 'no-store' });
      if (!res.ok) throw new Error(`Failed to load items (${res.status})`);
      const data = (await res.json()) as Item[];
      setItems(data);
    } catch (err) {
      setItems([]);
      setError(err instanceof Error ? err.message : 'Failed to load items');
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadItems();
  }, []);

  async function onSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const trimmed = title.trim();
    if (!trimmed) {
      setError('Title is required');
      return;
    }

    setSubmitting(true);
    setError(null);
    try {
      const res = await fetch(`${apiBase}/api/items`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title: trimmed }),
      });
      if (!res.ok) throw new Error(`Failed to create item (${res.status})`);
      const created = (await res.json()) as Item;
      setItems((current) => [...current, created]);
      setTitle('');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to create item');
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <main style={{ maxWidth: 720, margin: '40px auto', fontFamily: 'sans-serif' }}>
      <h1>Next.js + NestJS Starter</h1>
      <p>Thin first slice: create and list items through a NestJS API.</p>

      <form onSubmit={onSubmit} style={{ display: 'flex', gap: 12, margin: '24px 0' }}>
        <input
          value={title}
          onChange={(event) => setTitle(event.target.value)}
          placeholder="Add the next product task"
          style={{ flex: 1, padding: '10px 12px' }}
        />
        <button type="submit" disabled={submitting} style={{ padding: '10px 16px' }}>
          {submitting ? 'Saving...' : 'Add item'}
        </button>
      </form>

      {error ? <p style={{ color: 'crimson' }}>{error}</p> : null}
      {loading ? <p>Loading items...</p> : null}
      {!loading && items.length === 0 ? <p>No items yet.</p> : null}

      <ul>
        {items.map((item) => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>
    </main>
  );
}
