<template>
    <div class="container mt-4">
        <h2 class="text-center mb-4">Patient Management</h2>

        <!-- Add Patient Button -->
        <div class="mb-3 text-end">
            <button class="btn btn-primary" @click="toggleForm">
                {{ showForm ? 'Cancel' : 'Add Patient' }}
            </button>
        </div>

        <!-- Form Section -->
        <div v-if="showForm" class="card mb-4 shadow-sm">
            <div class="card-header bg-primary text-white">
                {{ editMode ? 'Edit Patient' : 'Add New Patient' }}
            </div>
            <div class="card-body">
                <form @submit.prevent="handleSubmit">
                    <div class="mb-3">
                        <label for="first_name" class="form-label">First Name</label>
                        <input v-model="form.first_name" type="text" id="first_name" class="form-control"
                            placeholder="Enter first name" required />
                    </div>
                    <div class="mb-3">
                        <label for="last_name" class="form-label">Last Name</label>
                        <input v-model="form.last_name" type="text" id="last_name" class="form-control"
                            placeholder="Enter last name" required />
                    </div>
                    <button type="submit" class="btn btn-success">
                        {{ editMode ? 'Update Patient' : 'Add Patient' }}
                    </button>
                    <button v-if="editMode" type="button" class="btn btn-secondary ms-2" @click="resetForm">
                        Cancel
                    </button>
                </form>
            </div>
        </div>

        <!-- Patient List Section -->
        <div class="card shadow-sm">
            <div class="card-header bg-secondary text-white">
                Patient List
            </div>
            <ul class="list-group list-group-flush">
                <li v-for="patient in patients" :key="patient.id"
                    class="list-group-item d-flex justify-content-between align-items-center">
                    <div>
                        <strong>{{ patient.first_name }} {{ patient.last_name }}</strong>
                    </div>
                    <div>
                        <button @click="editPatient(patient)" class="btn btn-warning btn-sm me-2">
                            Edit
                        </button>
                        <button @click="deletePatient(patient.id)" class="btn btn-danger btn-sm me-2">
                            Delete
                        </button>
                        <button @click="viewMedicalRecords(patient.id)" class="btn btn-info btn-sm">
                            View Medical Records
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
    data() {
        return {
            patients: [],
            form: { first_name: "", last_name: "" },
            editMode: false,
            editingPatientId: null,
            showForm: false, // Controls the visibility of the form
        };
    },
    created() {
        this.fetchPatients();
    },
    methods: {
        fetchPatients() {
            axios.get("http://127.0.0.1:8000/api/patients/").then((response) => {
                this.patients = response.data;
            });
        },
        handleSubmit() {
            if (this.editMode) {
                this.updatePatient();
            } else {
                this.addPatient();
            }
        },
        addPatient() {
            axios.post("http://127.0.0.1:8000/api/patients/", this.form).then(() => {
                this.fetchPatients();
                this.resetForm();
            });
        },
        editPatient(patient) {
            this.form.first_name = patient.first_name;
            this.form.last_name = patient.last_name;
            this.editMode = true;
            this.editingPatientId = patient.id;
            this.showForm = true; // Show the form when editing
        },
        updatePatient() {
            axios
                .put(
                    `http://127.0.0.1:8000/api/patients/${this.editingPatientId}/`,
                    this.form
                )
                .then(() => {
                    this.fetchPatients();
                    this.resetForm();
                });
        },
        deletePatient(id) {
            axios.delete(`http://127.0.0.1:8000/api/patients/${id}/`).then(() => {
                this.fetchPatients();
            });
        },
        resetForm() {
            this.form = { first_name: "", last_name: "" };
            this.editMode = false;
            this.editingPatientId = null;
            this.showForm = false; // Hide the form after resetting
        },
        toggleForm() {
            this.showForm = !this.showForm; // Toggle the visibility of the form
            if (!this.showForm) {
                this.resetForm(); // Reset the form if it's being hidden
            }
        },
        viewMedicalRecords(patientId) {
            this.$router.push({ name: "MedicalRecords", params: { patientId } });
        },
    },
};
</script>

<style>
/* Add custom styles if needed */
</style>