import React from 'react';
import { render } from '@testing-library/react';
import App from './App';

test('renders retard', () => {
  const { getByText } = render(<App />);
  const linkElement = getByText(/retarded/i);
  expect(linkElement).toBeInTheDocument();
});
