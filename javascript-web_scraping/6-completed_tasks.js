#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;

  const completedPerUser = {};
  const tasks = JSON.parse(body);
  const completed = tasks.filter(task => task.completed === true);

  completed.forEach(task => {
    completedPerUser[task.userId] = ++completedPerUser[task.userId] || 1;
  });

  console.log(completedPerUser);
});
