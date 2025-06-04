import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Form, FormControl, Button, Alert } from 'react-bootstrap';
import { useLocation } from 'react-router-dom';
import queryString from 'query-string';
import SearchResult from '../components/SearchResult';
import axios from 'axios';
import { Link } from "react-router-dom";

let getStringValue = (obj: string | string[] | null | undefined, defaultValue?: string): string => {
    if (obj == null) {
        if (defaultValue === undefined) {
            return ''
        }
        return defaultValue;
    }
    if (Array.isArray(obj)) {
        return obj[0];
    }
    return obj;
}


const SearchPage: React.FC<{}> = () => {
    const getSearchType = (location: any): string => {
        const params = queryString.parse(location.search);
        return getStringValue(params.t, 'person');
    }

    const getSearchQuery = (location: any): string => {
        const params = queryString.parse(location.search);
        return getStringValue(params.q);
    }

    const location = useLocation();
    const definedSearchQuery = getSearchQuery(location);
    const definedSearchType = getSearchType(location);

    const [searchQuery, setSearchQuery] = useState(definedSearchQuery);
    const [searchType, setSearchType] = useState(definedSearchType);
    const [searchResultInstance, setSearchResultInstance] = useState(undefined);
    const search = (searchQuery: string, searchType: string) => {
        axios.get(`${process.env.REACT_APP_NATURAL_LANG_API_HOST}/api/kb/${searchType}/search`, {
            params: {
                q: searchQuery,
            }
        })
            .then(res => {
                if (res.data.length > 0) {
                    setSearchResultInstance(res.data[0]);
                } else {
                    setSearchResultInstance(undefined);
                }
            })
            .catch(err => console.log(err));
    }

    useEffect(() => {
        if (definedSearchQuery) {
            search(definedSearchQuery, definedSearchType);
        }
    }, []);
    return (

        <Container fluid style={{ padding: '3rem' }}>

            <h4>Knowledge Base Search</h4>
            <Form method="get">
                <Row>
                    <Col md={8} sm={6}>
                        <FormControl type="text" placeholder="Search" className="mr-sm-2" name="q" value={searchQuery} onChange={e => setSearchQuery(e.target.value)} />
                    </Col>
                    <Col md={2} sm={4}>
                        <FormControl as="select" className="mr-sm-2" name="t" value={searchType} onChange={e => setSearchType(e.target.value)}>
                            <option value="person">Person</option>
                            <option value="organisation">Organisation</option>
                            <option value="role">Role</option>
                        </FormControl>
                    </Col>
                    <Col md={2} sm={2}>
                        <Button type="submit">Search</Button>
                    </Col>
                </Row>




            </Form>
            <Form.Text className="text-muted">
                Try <a href={`/search?q=Alan%20Turing&t=person`}>Alan Turing</a> or <a href={`/search?q=Google&t=organisation`}>Google</a>
            </Form.Text>
            {(definedSearchType && definedSearchQuery) && (
                searchResultInstance
                    ? <Row md={3} className="py-4">
                        <Col>
                            <SearchResult instance={searchResultInstance} />
                        </Col>
                    </Row>
                    : <Alert variant="light">No {definedSearchType} matches found for "{definedSearchQuery}"</Alert>)}
        </Container>
    )

}
export default SearchPage;