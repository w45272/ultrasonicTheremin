import './App.css';
import { WebSocketDemo } from './WebSocket.js'
import { NoteSocket } from './NoteSocket.js'

function App() {
  return (
    <div className="App">
        <NoteSocket/>
    </div>
  );
}

export default App;
