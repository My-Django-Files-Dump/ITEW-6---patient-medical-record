<template>
    <div class="container mt-4">
        <h2 class="text-center mb-4">Medical Records for Patient {{ patientName }}</h2>

        <div class="mb-4 text-end">
            <button class="btn btn-secondary" @click="goBackToPatientList">
                Back to Patient List
            </button>
        </div>

        <div class="mb-4 text-end">
            <button class="btn btn-primary" @click="toggleForm">
                {{ showForm ? 'Cancel' : 'Add New Medical Record' }}
            </button>
        </div>

        <div v-if="showForm" class="card mb-4 shadow-sm">
            <div class="card-header bg-primary text-white">
                {{ editMode ? 'Edit Medical Record' : 'Add New Medical Record' }}
            </div>
            <div class="card-body">
                <form @submit.prevent="handleSubmit">
                    <div class="mb-3">
                        <label for="diagnosis" class="form-label">Diagnosis:</label>
                        <input v-model="form.diagnosis" type="text" id="diagnosis" class="form-control"
                            placeholder="Enter diagnosis" required />
                    </div>
                    <div class="mb-3">
                        <label for="prescription" class="form-label">Prescription:</label>
                        <input v-model="form.prescription" type="text" id="prescription" class="form-control"
                            placeholder="Enter prescription" required />
                    </div>
                    <div class="mb-3">
                        <label for="visit_date" class="form-label">Visit Date:</label>
                        <input v-model="form.visit_date" type="date" id="visit_date" class="form-control" required />
                    </div>
                    <button type="submit" class="btn btn-success">
                        {{ editMode ? 'Update Record' : 'Add Record' }}
                    </button>
                    <button v-if="editMode" type="button" class="btn btn-secondary ms-2" @click="resetForm">
                        Cancel
                    </button>
                </form>
            </div>
        </div>

        <div class="card shadow-sm">
            <div class="card-header bg-secondary text-white">
                Medical Records List
            </div>
            <ul class="list-group list-group-flush">
                <li v-for="record in records" :key="record.id"
                    class="list-group-item d-flex justify-content-between align-items-center">
                    <div>
                        <strong>Diagnosis:</strong> {{ record.diagnosis }} <br />
                        <strong>Prescription:</strong> {{ record.prescription }} <br />
                        <strong>Visit Date:</strong> {{ record.visit_date }}
                    </div>
                    <div>
                        <button @click="editRecord(record)" class="btn btn-warning btn-sm me-2">
                            Edit
                        </button>
                        <button @click="deleteRecord(record.id)" class="btn btn-danger btn-sm">
                            Delete
                        </button>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    props: ["patientId"],
    data() {
        return {
            records: [],
            patientName: "",
            form: {
                diagnosis: "",
                prescription: "",
                visit_date: "",
                patient: null,
            },
            editMode: false,
            editingRecordId: null,
            showForm: false,
        };
    },
    created() {
        this.fetchPatientDetails(); 
        this.fetchRecords();
    },
    methods: {
        fetchPatientDetails() {
            axios
                .get(`http://127.0.0.1:8000/api/patients/${this.patientId}/`)
                .then((response) => {
                    this.patientName = `${response.data.first_name} ${response.data.last_name}`;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        fetchRecords() {
            axios
                .get(`http://127.0.0.1:8000/api/patients/${this.patientId}/records/`)
                .then((response) => {
                    this.records = response.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        handleSubmit() {
            if (this.editMode) {
                this.updateRecord();
            } else {
                this.addRecord();
            }
        },
        addRecord() {
            axios
                .post("http://127.0.0.1:8000/api/records/", {
                    ...this.form,
                    patient: this.patientId, 
                })
                .then(() => {
                    this.fetchRecords();
                    this.resetForm();
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        editRecord(record) {
            this.form.diagnosis = record.diagnosis;
            this.form.prescription = record.prescription;
            this.form.visit_date = record.visit_date;
            this.form.patient = this.patientId;
            this.editMode = true;
            this.editingRecordId = record.id;
            this.showForm = true;
        },
        updateRecord() {
            axios
                .put(
                    `http://127.0.0.1:8000/api/records/${this.editingRecordId}/`,
                    this.form 
                )
                .then(() => {
                    this.fetchRecords();
                    this.resetForm();
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        deleteRecord(recordId) {
            axios
                .delete(`http://127.0.0.1:8000/api/records/${recordId}/`)
                .then(() => {
                    this.fetchRecords();
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        resetForm() {
            this.form = {
                diagnosis: "",
                prescription: "",
                visit_date: "",
                patient: null,
            };
            this.editMode = false;
            this.editingRecordId = null;
            this.showForm = false;
        },
        toggleForm() {
            this.showForm = !this.showForm; 
            if (!this.showForm) {
                this.resetForm(); 
            }
        },
        goBackToPatientList() {
            this.$router.push({ name: "PatientManagement" }); 
        },
    },
};
</script>
