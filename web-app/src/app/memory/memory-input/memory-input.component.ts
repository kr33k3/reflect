import { Component, OnInit, Input } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Memory, Content } from 'src/app/models';
import { Title } from '@angular/platform-browser';


@Component({
  selector: 'app-memory-input',
  templateUrl: './memory-input.component.html',
  styleUrls: ['./memory-input.component.scss'],
})
export class MemoryInputComponent implements OnInit {
  @Input() memory: Memory
  memoryForm: FormGroup;


  constructor(private formBuilder: FormBuilder) {
   }

  ngOnInit() {
    this.memoryForm = this.formBuilder.group({
      'Title': [this.memory.Title, Validators.required],
      'Type': [this.memory.Type, Validators.required],
      'PageStart': [this.memory.PageStart, Validators.required],
      'PageEnd': [this.memory.PageEnd, Validators.required],
      'ContentList': [this.memory.ContentList, Validators.required],
      'DateCreated': [this.memory.DateCreated, Validators.required]
    })
    this.onChanged()
  }


  addContent() {
    this.memory.ContentList.push({
      Title: '',
      Body: '',
      Attachments: [],
      Tags: []
    });
   }

   removeContent(index) {
     console.log(this.memory.ContentList[index])
     this.memory.ContentList.splice(index, 1)
   }

   onChanged() {
    for (const field in this.memoryForm.controls) { // 'field' is a string
      console.log(field)
      this.memoryForm.get(field).valueChanges.subscribe(val => {
        this.memory[field] = val
      })
    }
   }

}
