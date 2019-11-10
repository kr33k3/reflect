import { Component, OnInit, Input } from '@angular/core';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Memory, Content } from 'src/app/models';


@Component({
  selector: 'app-memory-input',
  templateUrl: './memory-input.component.html',
  styleUrls: ['./memory-input.component.scss'],
})
export class MemoryInputComponent implements OnInit {
  @Input() memory: Memory
  contentList: Content[];
  memoryForm: FormGroup;


  constructor(private formBuilder: FormBuilder) {
    this.contentList = [{Title: "Other Title", Body: "YADADADADA", Tags:[], Attachments: [] }]
    if (this.memory == null) {
      this.memory = {
        Title: 'The Title',
        Type: 'The Type',
        ContentList: [],
        DateCreated: new Date()
      }
    }
    
    this.memoryForm = this.formBuilder.group({
      'Title': [this.memory.Title, Validators.required],
      'Type': [this.memory.Type, Validators.required],
      'ContentList': [this.contentList, Validators.required],
      'DateCreated': [this.memory.DateCreated, Validators.required]
    })   
   }

  ngOnInit() {}


  addContent() {
    console.log('PUSHING CONTENT');
    this.contentList.push(null);
   }

}
