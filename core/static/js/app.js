// Root React component
function App() {
    const [message, setMessage] = React.useState('Loading...');
    const [apiData, setApiData] = React.useState(null);
    const [isLoading, setIsLoading] = React.useState(true);
    const [error, setError] = React.useState(null);
    
    React.useEffect(() => {
        // Fetch data from our Django API endpoint
        fetch('/api/example/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setApiData(data);
                setMessage('Data loaded successfully!');
                setIsLoading(false);
            })
            .catch(error => {
                setError('Error fetching data: ' + error.message);
                setIsLoading(false);
            });
    }, []);
    
    return (
        <div className="row">
            <div className="col-md-12">
                <div className="card">
                    <div className="card-header bg-primary text-white">
                        <h2>Django + React Integration</h2>
                    </div>
                    <div className="card-body">
                        <h3>{message}</h3>
                        
                        {isLoading && (
                            <div className="alert alert-info">Loading data from API...</div>
                        )}
                        
                        {error && (
                            <div className="alert alert-danger">{error}</div>
                        )}
                        
                        {apiData && (
                            <div className="mt-4">
                                <h4>API Response:</h4>
                                <p><strong>Message:</strong> {apiData.message}</p>
                                
                                <h5>Items:</h5>
                                <ul className="list-group">
                                    {apiData.items.map((item, index) => (
                                        <li key={index} className="list-group-item">{item}</li>
                                    ))}
                                </ul>
                            </div>
                        )}
                        
                        <div className="mt-4">
                            <p>This is a React component being served by Django!</p>
                            <button 
                                className="btn btn-success" 
                                onClick={() => alert('React is working!')}
                            >
                                Click me!
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

// Render the App component to the DOM
const rootElement = document.getElementById('root');
const root = ReactDOM.createRoot(rootElement);
root.render(<App />);
