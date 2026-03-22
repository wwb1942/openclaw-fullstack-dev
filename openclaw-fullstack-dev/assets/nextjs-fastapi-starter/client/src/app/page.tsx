const apiBase = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

export default async function Page() {
  const res = await fetch(`${apiBase}/api/items`, { cache: 'no-store' });
  const items = res.ok ? await res.json() : [];

  return (
    <main style={{ maxWidth: 720, margin: '40px auto', fontFamily: 'sans-serif' }}>
      <h1>Feedback Tracker</h1>
      <p>Thin first slice: list items from FastAPI, then add create/update flows.</p>
      <ul>
        {items.map((item: { id: number; title: string }) => (
          <li key={item.id}>{item.title}</li>
        ))}
      </ul>
    </main>
  );
}
