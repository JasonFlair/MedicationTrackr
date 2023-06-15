import React, { useEffect, useState } from "react";
import axios from "axios";
import "./form.css";
import FormInput from "./FormInput";
import { toast, ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { BsFillTrashFill, BsFillPencilFill } from "react-icons/bs";
import { Redirect } from "react-router-dom";
import {
  SidebarWrapper,
  StyledContainer,
  StyledMenuItem,
  TableWrapper,
  Table,
  Tbody,
  Thead,
  Th,
  Td,
  Span
} from "./MedicalDoseElements";

const MedicalDose = ({ isAuthenticated }) => {
  const [rows, setRows] = useState([]);
  const [dose, setDose] = useState(true);
  const [addDose, setAddDose] = useState(false);
  const [medId, setMedId] = useState(0);
  const [values, setValues] = useState({
    frequency: 0,
    medicineName: "",
    numOfDays: 0,
    quantity: 0,
  });

  const inputs = [
    {
      id: 1,
      name: "medicineName",
      type: "text",
      placeholder: "Medicine Name",
      label: "Medicine Name",
    },
    {
      id: 2,
      name: "quantity",
      type: "number",
      placeholder: "Quantity Per Dose",
      label: "Quantity Per Dose",
    },
    {
      id: 3,
      name: "numOfDays",
      type: "number",
      placeholder: "Number of Days",
      label: "Number of Days",
    },
    {
      id: 4,
      name: "frequency",
      type: "number",
      placeholder: "Drug Frequency",
      label: "Frequency",
    },
  ];

  useEffect(() => {
    localStorage.setItem("ids", JSON.stringify([]));
    fetchUserMedicine();
  }, [dose]);

  if (!isAuthenticated) {
    return <Redirect to="/" />;
  }

  const fetchUserMedicine = () => {
    const url = `http://127.0.0.1:5000/all_medicines_by_user/${window.localStorage.id}`;
    axios
      .get(url)
      .then((res) => {
        setRows([...res.data.medicines_for_user]);
      })
      .catch((err) => console.log(err));
  };

  const handleOnClick = (e) => {
    const id = e.target.dataset.id;
    if (id === "dose-1") {
      setAddDose(false);
      setDose(true);
      //   const url = `http://127.0.0.1:5000/all_medicines_by_user/${window.localStorage.id}`;
      //   axios
      //     .get(url)
      //     .then((res) => {
      //       console.log(res.data.medicines_for_user);
      //       setRows([...res.data.medicines_for_user]);
      //     })
      //     .catch((err) => console.log(err));
    }
    if (id === "dose-2") {
      setDose(false);
      setAddDose(true);
    }
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    let data = {
      medicine_name: values.medicineName,
      user_id: window.localStorage.id,
      quantity: values.quantity,
      num_of_days: values.numOfDays,
      frequency: values.frequency,
    };
    const url = `http://127.0.0.1:5000/new_medicine`;
    axios
      .post(url, data)
      .then((res) => {
        setValues({
          ...values,
          medicineName: "",
          quantity: 0,
          numOfDays: 0,
          frequency: 0,
        });
      })
      .catch((err) => console.log(err));
  };

  const onChange = (e) => {
    setValues({ ...values, [e.target.name]: e.target.value });
  };

  const showToastMessage = () => {
    toast.success(
      "Successfully added medicine!",
      {
        position: toast.POSITION.TOP_RIGHT,
      },
      { delay: 500 }
    );
  };

  const editRow = (id, name) => {
    let data = {
      name,
      day_completed: true,
      user_id: window.localStorage.id,
    };
    console.log(data);
    const url = `http://127.0.0.1:5000/update_medication_status`;
    axios
      .post(url, data)
      .then((res) => {
        console.log(res);
        if (JSON.parse(localStorage.getItem("ids"))) {
          const ids = JSON.parse(localStorage.getItem("ids"));
          ids.push(id);
          localStorage.setItem("ids", JSON.stringify(ids));
          setMedId(id);
        }
        fetchUserMedicine();
      })
      .catch((err) => console.log(err));
  };

  const deleteRow = (id) => {
    let data = {
      medicine_id: id,
      user_id: window.localStorage.id,
    };
    const url = `http://127.0.0.1:5000/delete_medicine`;
    axios
      .post(url, data)
      .then((res) => {
        console.log(res);
        fetchUserMedicine();
      })
      .catch((err) => console.log(err));
  };
  return (
    <StyledContainer>
      <SidebarWrapper>
        <StyledMenuItem
          data-id="dose-1"
          onClick={handleOnClick}
          clickItem={dose}
        >
          Medicine Details
        </StyledMenuItem>
        <StyledMenuItem
          data-id="dose-2"
          onClick={(e) => handleOnClick(e)}
          clickItem={addDose}
        >
          Add Medicine
        </StyledMenuItem>
      </SidebarWrapper>
      {addDose && (
        <>
          <div className="form">
            <form onSubmit={handleSubmit}>
              <h1>Add Drug Dose</h1>
              {inputs.map((input) => (
                <FormInput
                  key={input.id}
                  {...input}
                  value={values[input.name]}
                  onChange={onChange}
                />
              ))}
              <button onClick={showToastMessage} >Submit</button>
            </form>
          </div>
        </>
      )}
      {dose && (
        <>
          <TableWrapper>
            <Table>
              <Thead>
                <tr>
                  <Th>Medicine Name</Th>
                  <Th>Frequency</Th>
                  <Th>Number of Days</Th>
                  <Th>Days Left</Th>
                  <Th>Days Taken</Th>
                  <Th>Completed For Today </Th>
                  <Th>Actions</Th>
                </tr>
              </Thead>
              <Tbody>
                {rows.map((row, idx) => {
                  return (
                    <tr key={idx}>
                      <Td>{row.name}</Td>
                      <Td>{row.quantity_to_be_taken}</Td>
                      <Td>{row.num_of_days}</Td>
                      <Td>{row.days_left}</Td>
                      <Td>{row.days_taken}</Td>
                      <Td>
                        <Span onClick={() => editRow(row.id, row.name)}>
                          {JSON.parse(localStorage.ids).includes(medId)? "Done": "Yes"}
                        </Span>
                      </Td>
                      <Td className="fit">
                        <span className="actions">
                          <BsFillTrashFill
                            className="delete-btn"
                            onClick={() => deleteRow(row.id)}
                          />
                          {/* <BsFillPencilFill
                            className="edit-btn"
                            onClick={() => editRow(idx)}
                          /> */}
                        </span>
                      </Td>
                    </tr>
                  );
                })}
              </Tbody>
            </Table>
          </TableWrapper>
        </>
      )}
      <ToastContainer />
    </StyledContainer>
  );
};

export default MedicalDose;