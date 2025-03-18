import Link from "next/link";

export default function Sidebar() {
  return (
    <aside className="w-64 h-screen bg-gray-800 text-white p-4">
      <nav>
        <ul className="space-y-2">
          {/* Dashboard Link */}
          <li className="hover:bg-gray-700 p-2 rounded">
            <Link href="/dashboard">Dashboard</Link>
          </li>

          {/* Timesheets Link */}
          <li className="hover:bg-gray-700 p-2 rounded">
            <Link href="/timesheets">Timesheets</Link>
          </li>

          {/* Reports Link */}
          <li className="hover:bg-gray-700 p-2 rounded">
            <Link href="/reports">Reports</Link>
          </li>

          {/* Projects Link */}
          <li className="hover:bg-gray-700 p-2 rounded">
            <Link href="/projects">Projects</Link>
          </li>
        </ul>
      </nav>
    </aside>
  );
}