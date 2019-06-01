import React from 'react';
import { Query } from 'react-apollo';
import gql from 'graphql-tag';

import Course from './Course';

const Courses = () => (
    <Query query={gql`
        {
            allArtists {
                edges {
                  node {
                    name
                  }
                }
              }
        }
    `}
    >

        {({ loading, error, data }) => {

            return data.allArtists.map((currentCourse) => (
                <Course course={currentCourse} />
            ));
        }}
    </Query>
);

export default Courses;