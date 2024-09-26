import React, { useState, useEffect } from 'react';
import { Unstable_Popup as BasePopup } from '@mui/base/Unstable_Popup';
import { styled } from '@mui/system';

function HighlightPopUp({ sentences, anchorEl, onClose }) {
  const open = Boolean(anchorEl);
  const id = open ? 'highlight-popup' : undefined;

  return (
    <BasePopup id={id} open={open} anchor={anchorEl}>
      <PopupBody className="bg-white shadow-lg rounded-lg p-4 w-full max-w-md">
      <button
        onClick={onClose}
        className="absolute top-2 text-gray-500 hover:text-gray-800"
      >
        X
      </button>
        <h3 className="text-lg font-semibold mb-2">Similar Sentences</h3>
        {sentences && sentences.length > 0 ? (
          <ul className="list-disc list-inside">
            {sentences.map((sentence, index) => (
                <li key={index} className="text-sm text-gray-700">{sentence}</li>
            ))}
          </ul>
        ) : (
          <p className="text-sm text-gray-600">No similar sentences found.</p>
        )}
      </PopupBody>
    </BasePopup>
  );
}

const PopupBody = styled('div')(
  ({ theme }) => `
    width: 70%;
    padding: 12px 16px;
    margin: 8px;
    border-radius: 8px;
    border: 1px solid #ccc;
    background-color: ${theme.palette.mode === 'dark' ? '#303740' : '#fff'};
    box-shadow: ${theme.palette.mode === 'dark' ? '0px 4px 8px rgb(0 0 0 / 0.7)' : '0px 4px 8px rgb(0 0 0 / 0.1)'};
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 0.875rem;
    z-index: 1;
    `,
);

const CloseButton = styled('button')`
    background: none;
    border: none;
    font-size: 1.2rem;
    cursor: pointer;
    color: #999;

    &:hover {
        color: #333;
    }
`;

export default HighlightPopUp;
