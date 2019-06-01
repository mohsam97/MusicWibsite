
import React from 'react';
import ApolloClient from 'apollo-boost';
import { ApolloProvider } from 'react-apollo';
import Courses from "./Courses"


const client = new ApolloClient({
    uri: "http://127.0.0.1:8000/api/"
});

const App = () => (
    <ApolloProvider client={client}>
        <div>
            <Courses />
        </div>
    </ApolloProvider>
)

export default App;