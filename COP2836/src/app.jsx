const continents = ['Georgia', 'The United States of America', 'China', 'Australia', 'New Zealand'];
const helloContinents = Array.from(continents, c => `Hello ${c}!`)
const message = helloContinents.join(' ');

const element = (
    <div title="Outer div">
        <h1>{message}</h1>
    </div>
);
    
ReactDOM.render(element, document.getElementById('contents'));