const { StaticApp} = require('@keystonejs/app-static');
const { Keystone } = require('@keystonejs/keystone');
const { GraphQLApp } = require('@keystonejs/app-graphql');
const { AdminUIApp } = require('@keystonejs/app-admin-ui');
const { MongooseAdapter: Adapter } = require('@keystonejs/adapter-mongoose');
const { Integer, Text } = require('@keystonejs/fields');
const PROJECT_NAME = 'movie-rating';
const adapterConfig = { mongoUri: 'mongodb://localhost/movie-rating' };


/**
 * You've got a new KeystoneJS Project! Things you might want to do next:
 * - Add adapter config options (See: https://keystonejs.com/keystonejs/adapter-mongoose/)
 * - Select configure access control and authentication (See: https://keystonejs.com/api/access-control)
 */

const keystone = new Keystone({
  name : PROJECT_NAME,
  adapter: new Adapter(adapterConfig),
});

keystone.createList("Movie", {
  fields: {
    title: {
      type: Text,
      isRequired: true,
      isUnique: true
    },
    rating: {
      type: Integer,
      isRequired: true,
      defaultValue: 10
    }
  }
});

module.exports = {
  keystone,
  apps: 
    [new GraphQLApp(), 
    new StaticApp({ path: '/', src:'public'}),
    new AdminUIApp({ name: PROJECT_NAME, enableDefaultRoute: true })],
};
