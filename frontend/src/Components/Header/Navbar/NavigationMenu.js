export default function NavigationMenu() {
  const items = ["home", "requests"];

  return (
    <div className="nav-menu">
      {items.map((item, key) => (
        <div key={key}>{item}</div>
      ))}
    </div>
  );
}
