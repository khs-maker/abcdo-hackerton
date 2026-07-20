import React from 'react';
import BlockRenderer from './components/BlockRenderer';
import uiSchema from './uiSchema.json';

// 재료(uiSchema)를 일꾼(BlockRenderer)에게 전달해서 최종 화면을 그리게 합니다!
export default function App() {
  return (
    <div style={{ backgroundColor: '#f0f2f5', minHeight: '100vh', padding: '20px 0' }}>
      <BlockRenderer blocks={uiSchema} />
    </div>
  );
}