export default function App() {
    
    
    const handleClick = () => {
    alert('Button was clicked!');
};
return (
    <main style={{
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: '100vh',
    fontFamily: 'system-ui, sans-serif',
    fontSize: '2rem',
    margin: 0,
    }}>
    VoiceXL

    <div>
      {/* Render the native HTML button with the click handler */}
    <button type="button" onClick={handleClick}>
        Click Me
    </button>
    </div>
    </main>
    
)
}
