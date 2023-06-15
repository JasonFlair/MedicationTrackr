import styled from "styled-components";
import { Link } from "react-router-dom";

export const StyledContainer = styled.div`
  margin-top: 80px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  background: #F7F8FC;
  position: relative;
  paddingLeft: 285px;
  padding-right: 2rem;
  width: 100%;
  min-height: 100vh;
  max-width: 100vw;
  box-sizing: border-box;
  &:@media (max-width: 768px): {
    padding-left: 0;
  }
`;

export const SidebarWrapper = styled.div`
  top: 0;
  left: 0;
  max-width: 255px;
  height: 100vh;
  background: #363740;
  z-index: 1;
  overflowx: hidden;
`;

export const StyledMenuItem = styled.div`
  padding: 1.25rem 2rem;
  background: ${({ clickItem }) => (clickItem ? "#9FA2B4" : "none")};
  display: flex;
  align-items: center;
  justify-content: flex-start;
  font-size: 1rem;
  color: ${({ clickItem }) => (clickItem ? "#DDE2FF" : "#A4A6B3")};
  cursor: pointer;
  width: 100%;
  border-left: ${({ clickItem }) => (clickItem ? "4px solid #DDE2FF" : "none")};
  &:hover: {
    background: #9fa2b4;
    color: #dde2ff;
    border-left: 4px solid #dde2ff;
  }
`;

export const StyledForm = styled.form`
  width: 50%;
  background: rgb(255, 255, 255);
  border-radius: 4px;
  padding-left: 106px;
  padding-top: 16px;
`;

export const SFormTitle = styled.span`
  font-size: 24px;
  font-weight: 600;
`;

export const SFormControl = styled.div`
  :first-of-type {
    margin-top: 16px;
  }
  :not(:last-of-type) {
    margin-bottom: 8px;
  }
`;

export const StyledLabel = styled.label`
  display: block;
  font-size: 14px;
  font-weight: 600;
  margin-left: 4px;
  margin-bottom: calc(8 / 4);
`;

export const StyledInput = styled.input`
  outline: none;
  border: 1px solid rgba(51, 51, 51, 0.3);
  width: 100%;
  padding: 8px;
  font-size: 14px;
  border-radius: 4px;
`;

export const StyledButton = styled.button`
  width: 100%;
  background: rgb(20, 20, 20);
  color: rgb(247, 247, 247);
  padding: 8px;
  display: flex;
  justify-content: center;
  border-radius: 4px;
  margin-top: 16px;
  cursor: pointer;
`;

export const SRedirect = styled.div`
  font-size: 12px;
  width: 100%;
  display: flex;
  justify-content: center;
  margin-top: 8px;
`;

export const TableWrapper = styled.div`
  width: 97%;
`;

export const Table = styled.table`
  display: block;
  overflow: hidden;
  table-layout: fixed;
  border-collapse: collapse;
  box-shadow: 0px 10px 10px #ccc;
  border-radius: 10px;
  white-space: nowrap;
  width: 100em;
  max-width: 80%;
  margin-top: 10px;
  margin-left: 80px;
  table-layout: auto;
  overflow-x: auto;
`;

export const Thead = styled.thead`
  background-color: #ccc;
  color: #222;
`;

export const Th = styled.th`
  padding: 0.8rem;
`;

export const Tbody = styled.tbody`
  & tr:hover {
    background-color: #eee;
  }
`;

export const Td = styled.td`
  padding: 0.8rem;
  border-top: 0.5px solid #ddd;
  overflow: hidden;
  text-overflow: ellipsis;
  &.expand {
    width: 100%;
  }
  &.label {
    border-radius: 3px;
    padding: 0.3rem;
    color: white;
  }
  &.label-draft {
    background-color: #777;
  }
  &.label-live {
    background-color: #42a942;
  }
  & span.actions {
    display: flex;
    justify-content: space-around;
  }
  & span.actions svg {
    cursor: pointer;
  }
  & span svg.delete-btn {
    color: #e10d05;
  }
`;

export const Span = styled.button`
  margin-top: 1rem;
  border: none;
  background-color: #1d4ed8;
  color: #fff;
  padding: 0.2rem 0.2rem;
  border-radius: 10px;
  cursor: pointer;
  box-shadow: 0px 5px 5px #ccc;
`;

// export const StyledForm = styled.form`
//   margin-top: 80px;
//   margin-left: 350px;
//   width: 500px;
//   height: 300px;
//   padding: 50px;
//   border-radius: 5px;
// `

// export const StyledLabel = styled.label`
//   display: block;
//   margin-bottom: 5px;
//   font-weight: bold;
//   color: ${props => props.invalid ? 'red' : 'black'};
//`

//  export const StyledInput = styled.input`
//   width: 100%;
//   padding: 10px;
//   border: 1px solid #ccc;
//   border-radius: 5px;
// `

// export const StyledButton = styled.button`
//   background-color: #4caf50;
//   color: white;
//   padding: 10px;
//   margin-top: 10px;
//   border: none;
//   border-radius: 5px;
//   cursor: pointer;
//   &:disabled {
//     opacity: 0.5;
//   }
//   &:enabled {
//     opacity: 1.0;
//   }
//   opacity: ${props => !props.enabled ? 0.5 : 1};
// `

// export const btnReset = css`
//     font-family: inherit;
//     outline: none;
//     border: none;
//     background: none;
//     letter-spacing: inherit;
//     color: inherit;
//     font-size: inherit;
//     text-align: inherit;
//     padding: 0;
// `;
