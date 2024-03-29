import React, { Component } from 'react';
import joi from 'joi-browser';
import Input from './input';
import Select from './select';

class Form extends Component {
	state = {
		data: {},
		errors: {}
	};

	validate = () => {
		const options = { abortEarly: false };
		const { error } = joi.validate(this.state.data, this.schema, options);
		if (!error) return null;
		const errors = {};
		for (let item of error.details) errors[item.path[0]] = item.message;
		return errors;
	};

	validateProperty = ({ name, value }) => {
		const obj = { [name]: value };
		const schema = { [name]: this.schema[name] };
		const { error } = joi.validate(obj, schema);
		return error ? error.details[0].message : null;
	};

	handleSubmit = (e) => {
		e.preventDefault();
		const errors = this.validate();
		this.setState({ errors: errors || {} });
		if (errors) return;
		this.doSubmit();
	};

	handleChange = ({ currentTarget: input }) => {
		const errors = { ...this.state.errors };
		const errorMessage = this.validateProperty(input);
		if (errorMessage) errors[input.name] = errorMessage;
		else delete errors[input.name];

		const data = { ...this.state.data };
		data[input.name] = input.value;
		this.setState({ data, errors });
	};

	renderInput(name, label, type,inputForm,placeholder) {
		const { data, errors } = this.state;
		return (
			<Input
				label={label}
				name={name}
				type={type}
				value={data[name]}
				onChange={this.handleChange}
				error={errors[name]}
				className={inputForm}
				placeholder = {placeholder}
			/>
		);
	}

	renderSelect(name, label, options) {
		const { data, errors } = this.state;
		return (
			<Select
				name={name}
				value={data[name]}
				label={label}
				options={options}
				onChange={this.handleChange}
				error={errors[name]}
			/>
		);
	}

	renderButton(label) {
		return (
			<button disabled={this.validate()} className="btn btn-primary mb-2">
				{label}
			</button>
		);
	}
}

export default Form;
