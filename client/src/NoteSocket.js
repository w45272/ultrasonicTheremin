import React, { useState, useCallback, useEffect } from 'react';
import useWebSocket, { ReadyState } from 'react-use-websocket';
import { Input } from 'reactstrap';
export const NoteSocket = () => {
  const [socketUrl, setSocketUrl] = useState('ws://localhost:5000/note');
  const [messageHistory, setMessageHistory] = useState([]);
  const { sendMessage, lastMessage, readyState } = useWebSocket(socketUrl);

  useEffect(() => {
    if (lastMessage !== null) {
      setMessageHistory((prev) => prev.concat(lastMessage));
    }
  }, [lastMessage, setMessageHistory]);

  // const handleClickChangeSocketUrl = useCallback(
  //   () => setSocketUrl('ws://localhost:5000/note'),
  //   []
  // );
  const handleClickChangeSocketUrl = () => {
    
  };
  // const handleClickSendMessage = useCallback(() => sendMessage('Hello'), []);

  const connectionStatus = {
    [ReadyState.CONNECTING]: 'Connecting',
    [ReadyState.OPEN]: 'Open',
    [ReadyState.CLOSING]: 'Closing',
    [ReadyState.CLOSED]: 'Closed',
    [ReadyState.UNINSTANTIATED]: 'Uninstantiated',
  }[readyState];

  return (
    <div>
      <button onClick={handleClickChangeSocketUrl}>
        Click Me to change Socket Url
      </button>
      <Input
        value = {socketUrl}
        onChange={(e) => {setSocketUrl(e.target.value)}}
      >
      </Input><br>
      <span> The Socket URL is currently {socketUrl}</span><br>
      <span>The WebSocket is currently {connectionStatus}</span><br>
      {lastMessage ? <span>Last message: {lastMessage.data}</span> : null}
      {/* <ul> */}
      {/*   {messageHistory.map((message, idx) => ( */}
      {/*     <span key={idx}>{message ? message.data : null}</span> */}
      {/*   ))} */}
      {/* </ul> */}
    </div>
  );
};
